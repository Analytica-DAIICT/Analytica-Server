//selecting all required elements
const dropArea = document.querySelector(".drag-area"),
  dragText = dropArea.querySelector("header"),
  button = dropArea.querySelector(".file-select-btn"),
  submitBtn = dropArea.querySelector(".drag-area-submit-btn"),
  box3=document.querySelector(".box3"),
  box2p=document.querySelector(".box2-p"),
  uplodedfiles=document.querySelector(".uploaded-files"),
  input = dropArea.querySelector("input");
let files = [];
submitBtn.classList.add("hidden");
// box3.classList.add("hidden");
// box2p.classList.remove("hidden");
// uplodedfiles.classList.remove("hidden");

// Menubar upload data btn
document.querySelector(".upload-data-btn").addEventListener("click", () => {
  input.click();
});

button.onclick = () => {
  input.click(); //if user click on the button then the input also clicked
};

input.addEventListener("change", function () {
  files = this.files;
  console.log(files);
  dropArea.classList.add("active");
  showFile(); //calling function
});

//If user Drag File Over DropArea
dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File(s)";
});

//If user leave dragged File from DropArea
dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File(s)";
});

//If user drop File on DropArea
dropArea.addEventListener("drop", (event) => {
  event.preventDefault();
  files = event.dataTransfer.files;
  showFile();
});

function showFile() {
  let validExtensions = ["application/pdf", "application/vnd.ms-excel"]; //adding some valid image extensions in array
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    let fileType = file.type;
    // console.log(fileType);
    if (validExtensions.includes(fileType)) {
      let previewBox = document.querySelector(".uploaded-files");
      previewBox.innerHTML += `<p>${file.name}</p>`;
    } else {
      alert("This is not an PDF/CSV File!");
      dropArea.classList.remove("active");
      dragText.textContent = "Drag & Drop to Upload File";
      return;
    }
  }
  submitBtn.classList.remove("hidden");
  button.classList.add("hidden");
}

submitBtn.addEventListener("click", () => {
  box2p.classList.add("hidden")
  // uplodedfiles.classList.add("hidden")
  // box3.classList.remove("hidden");
});