goodPasswordMaterial = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g"
];
function generatePassword(material){
  goodPasswordMaterial.forEach((item, i) => {

    if (i % 2 == 0){
      goodPasswordMaterial[i] = item.toUpperCase() + i;
    }

  });
  return goodPasswordMaterial.toString();
}
document.cookie = `${generatePassword(goodPasswordMaterial)};expires=none; SameSite=None; Secure`



