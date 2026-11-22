// Render the newspaper page into the entry image.
//
// Reads index.html from this folder and screenshots it at 1024x1024
// with headless Chromium, writing entry.png beside it. Run with:
//     node generate.mjs
// Needs the playwright package (chromium) installed where Node can
// find it. The render is deterministic: same page, same pixels.

import { chromium } from "playwright";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const SIDE = 1024;

const folder = dirname(fileURLToPath(import.meta.url));
const pagePath = join(folder, "index.html");
const imagePath = join(folder, "entry.png");

const browser = await chromium.launch();
try {
  const page = await browser.newPage({
    viewport: { width: SIDE, height: SIDE },
    deviceScaleFactor: 1,
  });
  await page.goto(`file://${pagePath}`, { waitUntil: "load" });
  await page.waitForTimeout(500);
  await page.screenshot({ path: imagePath });
  console.log(`rendered ${imagePath} at ${SIDE}x${SIDE}`);
} finally {
  await browser.close();
}
