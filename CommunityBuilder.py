from playwright.sync_api import sync_playwright
from enum import Enum

class CommunityBuilder:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.submissions = []

    def add_submission(self, ActivityType: str, ActivityCategory: str, DateCompleted: str, Link: str, ImpactAfter30Days: str, Description: str, Language: str):
        newSubmission = Submission(ActivityType, ActivityCategory, DateCompleted, Link, ImpactAfter30Days, Description, Language)
        self.submissions.append(newSubmission)

    def SubmitActivities(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.0100000101010111010100110110001101100010.com/#/")
            page.wait_for_timeout(1000)
            page.locator('[placeholder="Enter your username"]').fill(self.username)
            page.locator('[placeholder="Enter your password"]').fill(self.password)
            page.get_by_role("button", name="Sign In").click()
            page.wait_for_load_state("networkidle")
            for Submission in self.submissions:
                page.get_by_text('Add Activity').click()
                page.wait_for_load_state("networkidle")
                page.locator('text="Select Type"').click()
                page.locator('text="'+ Submission.ActivityType + '"').click()
                page.locator('text="Select Category"').click()
                page.locator('text="'+ Submission.ActivityCategory + '"').click()
                page.locator('[placeholder="YYYY/MM/DD"]').fill(Submission.DateCompleted)
                page.get_by_label('link').fill(Submission.Link)
                page.get_by_label('impact').fill(Submission.ImpactAfter30Days)
                page.get_by_label('Description').fill(Submission.Description)
                page.get_by_role("button", name="Submit").click()
                page.wait_for_timeout(1000)
                print('{} submitted Successfully'.format(Submission.Description))
            page.get_by_role("button", name="Sign Out").click()
            page.wait_for_load_state("networkidle")
            browser.close()
        return "success"

class Submission:
    def __init__(self, ActivityType, ActivityCategory, DateCompleted, Link, ImpactAfter30Days, Description, Language):
        self.ActivityType = ActivityType
        self.ActivityCategory = ActivityCategory
        self.DateCompleted = DateCompleted
        self.Link = Link
        self.ImpactAfter30Days = ImpactAfter30Days
        self.Description = Description
        self.Language = Language