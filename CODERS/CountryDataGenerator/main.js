"strict";

const generateBtn = document.querySelector(".GenerateBtn");
const input = document.querySelector(".InputBox");
const CardBox = document.querySelector(".CountryCardBox");
const body = document.body;

generateBtn.addEventListener("click", async function (e) {
  e.preventDefault();
  try {
    const res = await fetch(
      `https://restcountries.com/v3.1/name/${input.value}`
    );
    if (!res.ok) {
      throw new Error(
        "Something went wrong, try to check your internet connection"
      );
    }
    const [data] = await res.json();

    console.log(Object.values(Object.values(data.currencies)[0])[0]);

    const html = `<div class="CountryCard">
       <img src="${data.flags.png}" alt="${input.value} flag"  >
       <div class = "CountryInfo">
       <h1>${input.value.toUpperCase()}</h1>
       <h2>${data.continents[0]} continent</h2> 
       <h3> 👬 ${(data.population / 1000000).toFixed(1)} Million People</h3>
       <h3> 🗣 ${Object.values(data.languages)} language</h3>
       <h3> 💰 ${Object.values(Object.values(data.currencies)[0])[0]}</h3>
       </div>
       </div>`;

    CardBox.insertAdjacentHTML("beforeend", html);
  } catch (error) {
    console.log(error.message);
  }
});

if (module.hot) {
  module.hot.accept();
}

//Netlify is a platform that allow we developers to host our application on CDN(content delivery network so it can be available and accessible anywhere)

//Git is a version control that create local repositories for easy tracking of changes in sourece code for application development

//Github is a open source repository where local repositories(git) are made available (Open-source) for other developers and can be changed. Basically, to ensure we have our code secure from being lost
