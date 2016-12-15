from hc.test import BaseTestCase
from hc.api.models import Check


class SwitchTeamTestCase(BaseTestCase):

    def test_it_switches(self):
        c = Check(user=self.alice, name="This belongs to Alice")
        c.save()

        self.client.login(username="bob@example.org", password="password")

        url = "/accounts/switch_team/%s/" % self.alice.username
        r = self.client.get(url, follow=True)

        ### Assert the contents of 
        self.assertIn(b'<!DOCTYPE html>\n<html lang="en">',r.content)
        self.assertIn(b'<head>',r.content)
        self.assertIn(b'<title>',r.content)
        self.assertIn(b'<meta name="description" content="Monitor and Get Notified When Your Cron Jobs Fail. Free alternative to Cronitor and Dead Man\'s Snitch.">\n',r.content)



    def test_it_checks_team_membership(self):
        self.client.login(username="charlie@example.org", password="password")

        url = "/accounts/switch_team/%s/" % self.alice.username
        r = self.client.get(url)
        ### Assert the expected error code
        self.assertEqual(r.status_code,403)

    def test_it_switches_to_own_team(self):
        self.client.login(username="alice@example.org", password="password")

        url = "/accounts/switch_team/%s/" % self.alice.username
        r = self.client.get(url, follow=True)
        ### Assert the expected error code
        self.assertEqual(r.status_code,200)
