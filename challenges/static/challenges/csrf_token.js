import Cookies from "js-cookie";
var CSRF_TOKEN = Cookies.get("csrftoken");
export default CSRF_TOKEN;
