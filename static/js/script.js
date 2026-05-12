console.log("Website Portfolio has been loaded and is running !");

const projButton = document.querySelector("button");

projButton.addEventListener("click", function () {
    const projectSection =
    document.querySelector("#projects");

    projectSection.scrollIntoView({
        behavior: "smooth"
    });

});