function convertCurrency() {
    // Get the exchange rates and JPY input values from the user
    let usdToJpy = document.getElementById("usdToJpy").value;
    let usdToMmk = document.getElementById("usdToMmk").value;
    let jpyAmount = document.getElementById("jpyInput").value;

    // Validate inputs
    if (usdToJpy === "" || usdToMmk === "" || jpyAmount === "" || isNaN(usdToJpy) || isNaN(usdToMmk) || isNaN(jpyAmount)) {
        document.getElementById("result").innerHTML = "Please enter valid amounts!";
        return;
    }

    // Convert JPY to USD
    let usdAmount = jpyAmount / usdToJpy;

    // Convert USD to MMK
    let mmkAmount = usdAmount * usdToMmk;

    // Display the result below the Convert button
    document.getElementById("result").innerHTML = `${jpyAmount} JPY = ${mmkAmount.toFixed(2)} MMK`;
}

