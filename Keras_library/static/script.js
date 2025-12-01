let selectedFile = null;

document.getElementById("fileInput").addEventListener("change", (event) => {
    selectedFile = event.target.files[0];

    const reader = new FileReader();
    reader.onload = (e) => {
        document.getElementById("preview").src = e.target.result;
    };
    reader.readAsDataURL(selectedFile);
});

async function sendToServer() {
    if (!selectedFile) {
        alert("Choose an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    const res = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("result").innerHTML =
        "Predicted Digit: <b>" + data.prediction + "</b>";
}
