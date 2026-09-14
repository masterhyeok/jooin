function onLoad() {
  const clicker = document.querySelector("#clicker")
  const add = document.querySelector("#add")
  const sumbit = document.querySelector("#sumbit")

  let v = 0

  add.addEventListener("click", () => {
    v += 1;
    clicker.innerHTML = v;
  });

  sumbit.addEventListener("click", function() {
      location.href='http://10.150.0.254:5002/'+v
      n = 0;
      num.innerHTML = v;
  })
}

window.addEventListener("load", onLoad);

