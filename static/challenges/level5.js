goodPasswordMaterial = [
  "d",
  "g",
  "i",
  "q",
  "f",
  "a",
  "o"
];

function generatePassword(material){
  goodPasswordMaterial.forEach((item, i) => {
    if (i % 2 == 0){
      goodPasswordMaterial[i] = item.toUpperCase() + i;
    }

  });

  password = ''
  for (i of goodPasswordMaterial) {
    password += i
  }

  return password;
}

document.cookie = `P4$$\\/\\/0RD=${generatePassword(goodPasswordMaterial)}; expires=none; SameSite=Lax;`


