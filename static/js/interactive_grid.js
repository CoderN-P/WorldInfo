const searchInput = document.querySelector('input');
myArray = [];
let counter = 1;
const dNone = 'd-none';
const imageListItems = document.querySelectorAll("#country-div");
console.log(imageListItems);
const captions = document.querySelectorAll("#country-name p");
console.log(captions);
for (const caption of captions) {
  myArray.push({
    id: counter++,
    text: caption.textContent
  });
}

searchInput.addEventListener("keyup", keyupHandler);

function keyupHandler() {
  console.log('hi');
  for (const item of imageListItems) {
    item.classList.add(dNone);
  }
  const text = this.value;
  const filteredArray = myArray.filter(el => el.text.includes(text));
  console.log(filteredArray);
  if (filteredArray.length > 0) {
    for (const el of filteredArray) {
      console.log(el.id);
      let a = document.querySelector(`#country-list a:nth-child(${el.id})`).children[0];

      a.classList.remove(dNone);
    }
  }
}