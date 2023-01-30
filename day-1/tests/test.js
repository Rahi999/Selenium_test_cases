const {By,Key,Builder} = require("selenium-webdriver");
require("chromedriver");

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
 