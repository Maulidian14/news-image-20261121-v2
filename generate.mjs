// Renders index.html to entry.png (1024x1024) using the local Chromium
// through Playwright. Run: node generate.mjs
import { chromium } from 'playwright-core';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));

async function render() {
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-dev-shm-usage',
      '--hide-scrollbars',
      '--force-device-scale-factor=1',
      '--allow-file-access-from-files',
    ],
  });
  try {
    const page = await browser.newPage({
      viewport: { width: 1024, height: 1024 },
      deviceScaleFactor: 1,
    });
    const problems = [];
    page.on('pageerror', (err) => problems.push(String(err)));
    await page.goto('file://' + join(here, 'index.html'), {
      waitUntil: 'load',
      timeout: 60000,
    });
    await page.waitForTimeout(800);
    await page.screenshot({ path: join(here, 'entry.png'), type: 'png' });
    if (problems.length > 0) {
      console.log('PAGE ERRORS:', problems.join(' | '));
    }
    console.log('rendered entry.png');
  } finally {
    await browser.close();
  }
}

await render();
