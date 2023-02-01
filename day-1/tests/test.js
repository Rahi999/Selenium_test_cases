const {By,Key,Builder} = require("selenium-webdriver");
require("chromedriver");

const USERNAME = "ahilh871";
const KEY = 'E3AzQrTMDiBPtYIZ7OhqNRSSqGjh0SpnTSFuF6oXoVk6LW2ki7';
const GRID_HOSt

const testFunction = async () => {
    const searchString = "Masai School Admission";
    let driver = await new Builder().forBrowser("chrome").build();

    await driver.get("https://www.google.com")
    await driver.findElement(By.name("q")).sendKeys(searchString,Key.RETURN);

    var title = await driver.getTitle();
    console.log("Title is :",title);

    setTimeout(() => {
         driver.quit()
    }, 5000)

}
testFunction()
 