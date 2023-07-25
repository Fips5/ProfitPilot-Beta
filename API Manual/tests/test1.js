const puppeteer = require('puppeteer');

async function scrapeWebsite() {
  const browser = await puppeteer.launch(); // Launch a headless browser
  const page = await browser.newPage(); // Create a new page instance
  await page.goto('https://www.etoro.com/markets/tsla'); // Navigate to the target URL

  setInterval(async () => {
    const [element] = await page.$x('/html/body/app-root/et-layout-main/div/div[2]/div[2]/div[3]/div/ui-layout/ng-view/et-market-page/div/et-market-page-header/div/div/et-header-instrument-avatar/div/div[2]/div/span[1]');
    // Select the element using the provided XPath

    if (element) { // Check if the element is found
      const text = await page.evaluate(element => element.textContent, element);
      // Extract the text content of the element
      console.log('Data:', text);
    } else {
      console.log('Element not found');
    }
  }, 60000); // Fetch data every minute

  // Keep the script running indefinitely
  // You can exit the script manually by pressing Ctrl+C
}

scrapeWebsite();
