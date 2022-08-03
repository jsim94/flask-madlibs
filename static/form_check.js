inputForm = document.querySelector("form");
inputForm.addEventListener("submit", checkInputs);

function checkInputs(e) {
  textboxList = document.querySelectorAll("input[type=text]");

  for (let i = 0; i < textboxList.length; i++) {
    let txt = textboxList[i].value;

    if (txt.length < 3) {
      e.preventDefault();
      alert("Incomplete Form! - Minimum 3 characters");
      console.log("click");
      return;
    }
    textboxList[i].value = txt.toLowerCase();
  }
}
