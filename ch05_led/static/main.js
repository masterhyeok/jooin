function onLoad() {
    const stateImg = document.querySelector("#state-img");
    const stateTxt = document.querySelector("#state-txt");

    const ledOn = document.querySelector("#led-on");
    const ledOff = document.querySelector("#led-off");

    let val = false;

    function onChange(nval = false) {
        stateImg.src = nval ? "/static/on.png" : "/static/off.png";
        stateTxt.textContent = nval ? "on" : "off";

        if (val !== nval) {
            fetch("http://10.150.0.254:5002/led", {method: "PATCH", body: nval ? "1" : "0"});
        }

        val = nval;
    }

    ledOn.addEventListener("click", () => {
        onChange(true);
    });

    ledOff.addEventListener("click", () => {
        onChange(false);
    })
}

window.addEventListener('load', onLoad);
