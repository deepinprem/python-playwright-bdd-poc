import { test, expect } from '@playwright/test';
import path from 'path';
import { pathToFileURL } from 'url';

test('Kindergarten Enrollment Submission', async ({ page }) => {
    const filePath = path.join(__dirname, 'fixtures', 'mock_enrollment.html');
    await page.goto(pathToFileURL(filePath).href);
    
    // Pause to see the empty form open
    await page.waitForTimeout(2000);

    // Type name slowly and pause
    await page.fill('#childName', 'Chandni Premkumar');
    await page.waitForTimeout(2000);

    // Click submit and pause to see the success message
    await page.click('#submitBtn');
    await page.waitForTimeout(3000);

    const header = page.locator('#header');
    await expect(header).toBeVisible();
    await expect(header).toHaveText('Student Chandni Premkumar submitted application for Kindergarden successfully');
});