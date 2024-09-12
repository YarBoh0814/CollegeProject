function convertCurrency() {
    // Get the exchange rates and JPY input values from the user
    let usdToMmk = document.getElementById("usdToMmk").value;
    let usdToJpy = document.getElementById("usdToJpy").value;
    let jpyAmount = document.getElementById("jpyInput").value;

    // Validate inputs
    if (usdToMmk === "" || usdToJpy === "" || jpyAmount === "" || isNaN(usdToMmk) || isNaN(usdToJpy) || isNaN(jpyAmount)) {
        document.getElementById("result").innerHTML = "Please enter valid amounts!";
        return;
    }

    // Convert JPY to USD
    let usdAmount = jpyAmount / usdToJpy;

    // Convert USD to MMK
    let mmkAmount = usdAmount * usdToMmk;

    // Display the result in the format: JPY = MMK
    document.getElementById("result").innerHTML = `${jpyAmount} JPY = ${mmkAmount.toFixed(2)} MMK`;
}
