const handleAlerts = (type, msg) => {
    alerBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}