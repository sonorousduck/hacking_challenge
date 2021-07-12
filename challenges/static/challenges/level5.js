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

  console.log(password)
  return password;
}
document.cookie = `${generatePassword(goodPasswordMaterial)};expires=none; SameSite=Lax;`



