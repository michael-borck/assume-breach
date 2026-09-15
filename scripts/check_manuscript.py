#!/usr/bin/env python3
"""Read-only source checks for Assume Breach; no model, network or lab required."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONFIG = (ROOT / "_quarto.yml").read_text()
FILES = re.findall(r"^\s*-\s+([^\s]+\.qmd)\s*$", CONFIG, re.M)
CORE = [name for name in FILES if name.startswith("chapters/")]
CASE = (ROOT / "appendices/defender-dossier.qmd").read_text()


def minutes(clock):
    hour, minute = map(int, clock.split(":"))
    return hour * 60 + minute


def table_rows(text):
    return [[cell.strip() for cell in line.strip("|").split("|")]
            for line in text.splitlines() if line.startswith("|")]


def decide(rules, flow):
    for source, destination, service, action in rules:
        if all(rule == "Any" or rule == value
               for rule, value in zip((source, destination, service), flow)):
            return action
    return "Deny"


class ManuscriptChecks(unittest.TestCase):
    def test_configured_order_and_files(self):
        self.assertEqual(len(FILES), len(set(FILES)))
        self.assertEqual(len(CORE), 12)
        self.assertEqual([int(Path(p).name[:2]) for p in CORE], list(range(1, 13)))
        self.assertEqual(len(FILES), 19)
        for name in FILES:
            self.assertTrue((ROOT / name).is_file(), name)

    def test_links_and_source_images(self):
        for name in FILES:
            source = ROOT / name
            for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source.read_text()):
                if target.startswith(("https://", "http://", "#")):
                    continue
                path, _, anchor = target.partition("#")
                dest = source.parent / path
                self.assertTrue(dest.is_file(), f"{name}: {target}")
                if anchor and dest.suffix == ".qmd":
                    self.assertIn("{" + "#" + anchor, dest.read_text(),
                                  f"{name}: {target}")

    def test_distinct_practice_and_optional_ai(self):
        chapters = [(ROOT / name).read_text() for name in CORE]
        self.assertEqual(sum("## Take it to the AI" in t for t in chapters), 3)
        for text in chapters:
            self.assertIn("## Questions to consider", text)
            self.assertIn("defender-dossier.qmd", text)
            self.assertTrue(re.search(r"\d+(?:–\d+)?(?: minutes|-minute)", text),
                            "A chapter is missing its timed practice task")
        self.assertIn("eight checks", CASE)
        self.assertIn("no software installation", (ROOT / "index.qmd").read_text())

    def test_safety_and_notification_boundaries(self):
        intro = (ROOT / "index.qmd").read_text()
        lab = (ROOT / "appendices/lab-environment.qmd").read_text()
        web = (ROOT / CORE[8]).read_text()
        self.assertIn("Do not paste real phishing emails", intro)
        self.assertIn("NAT allows outbound access to the host/LAN and internet", lab)
        self.assertIn("Host-only connects guests to the host", lab)
        self.assertIn("If scope is unclear, stop", lab)
        self.assertIn("not a general waiting period", web)
        self.assertIn("Processors notify the controller", web)
        self.assertIn("A vulnerability can lead to a privacy incident", web)

    def test_budget_and_expected_loss(self):
        rows = [row for row in table_rows(CASE) if re.match(r"^[ABCD]:", row[0])]
        costs = {row[0][0]: int(re.sub(r"[^\d]", "", row[1])) for row in rows}
        self.assertEqual(costs, {"A": 1000, "B": 800, "C": 1200, "D": 1000})
        self.assertEqual(sum(costs[k] for k in "ABC"), 3000)
        self.assertEqual(costs["A"] + costs["C"], 2200)
        self.assertGreater(sum(costs[k] for k in "ABC"), 2200)
        self.assertAlmostEqual(50000 * (.10 - .04) - costs["A"], 2000)
        self.assertAlmostEqual(50000 * (.10 - .09) - costs["A"], -500)
        self.assertAlmostEqual(50000 * (.10 - .02) - costs["A"], 3000)
        self.assertAlmostEqual(.10 - costs["A"] / 50000, .08)
        self.assertAlmostEqual(80000 * (.10 - .06) - costs["A"], 2200)
        for number in [r"\$5,000", r"\$2,000", r"\$8,000", r"\$4,800"]:
            self.assertIn(number, CASE)

    def test_recovery_arithmetic_and_failed_readiness(self):
        clocks = [row[0] for row in table_rows(CASE)
                  if re.fullmatch(r"\d\d:\d\d", row[0])]
        self.assertIn("09:20", clocks)
        self.assertIn("11:50", clocks)
        self.assertEqual(minutes("11:50") - minutes("09:20"), 150)
        self.assertEqual((minutes("09:20") - minutes("23:00")) % 1440, 620)
        self.assertEqual(minutes("09:20") - minutes("09:00"), 20)
        self.assertEqual(10 + 100 + 20, 130)
        self.assertGreater(130, 2 * 60)
        for phrase in ["**150 minutes**", "**620 minutes**", "**20 minutes**",
                       "**130 minutes**", "**10 minutes**", "not ready"]:
            self.assertIn(phrase, CASE)

    def test_printed_firewall_policy(self):
        rules = [row[1:] for row in table_rows(CASE)
                 if len(row) == 5 and row[0].isdigit()]
        self.assertEqual(len(rules), 5)
        allowed = [
            ("Public", "Web", "HTTPS"),
            ("Web", "Booking database", "Database"),
            ("Staff", "VPN gateway", "VPN"),
            ("Guest", "Internet", "HTTPS"),
        ]
        denied = [
            ("Guest", "Booking database", "Database"),
            ("Public", "Booking database", "Database"),
            ("Public", "Web", "Database"),
        ]
        self.assertEqual([decide(rules, flow) for flow in allowed + denied],
                         ["Allow", "Allow", "Allow", "Deny",
                          "Allow", "Allow", "Deny"])
        corrected = [(*flow, "Allow") for flow in allowed]
        self.assertEqual([decide(corrected, flow) for flow in allowed + denied],
                         ["Allow"] * 4 + ["Deny"] * 3)
        self.assertIn("first matching rule decides", CASE)
        self.assertIn("Do not copy this teaching notation into a firewall", CASE)

    def test_downloads_and_copyright(self):
        self.assertIn('license: "CC BY 4.0 International"', CONFIG)
        for name in ["copyright.qmd", "copyright-page.tex"]:
            text = (ROOT / name).read_text()
            self.assertIn("Creative Commons Attribution 4.0 International", text)
            self.assertIn("https://creativecommons.org/licenses/by/4.0/", text)
        for ext in ["pdf", "epub"]:
            self.assertIn(f"href: /assume-breach.{ext}", CONFIG)
        self.assertIn("copyright.qmd", FILES)
        self.assertIn('unless-format="pdf"', (ROOT / "copyright.qmd").read_text())
        for name in FILES:
            self.assertNotIn("—", (ROOT / name).read_text(), name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
