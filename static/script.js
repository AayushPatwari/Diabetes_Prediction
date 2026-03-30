function predict() {

  const ids = ["preg","glucose","bp","skin","insulin","bmi","dpf","age"];
  for (let id of ids) {
    if (document.getElementById(id).value === "") {
      result.innerText = "Fill all fields"
      return;
    }
  }

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pregnancies: Number(preg.value),
      glucose: Number(glucose.value),
      bloodpressure: Number(bp.value),
      skin: Number(skin.value),
      insulin: Number(insulin.value),
      bmi: Number(bmi.value),
      dpf: Number(dpf.value),
      age: Number(age.value)
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      result.innerText = "Error: " + data.error;
    } else {
      result.innerText = "Prediction Result: " + data.prediction;
    }
  })
  .catch(err => {
    console.error(err);
    result.innerText = "Server not responding";
  });
}
