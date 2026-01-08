const adminBtn = document.querySelector(".btn-warning");
const adminMessage = document.getElementById("adminMessage");

adminBtn.addEventListener("click", () => {
  adminMessage.innerHTML =
    `<div class="alert alert-success">Manual sync completed</div>`;
});
