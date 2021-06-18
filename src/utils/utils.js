var utils = {
  emailReg : /^[a-z0-9A-Z]+([-|_|.]+[a-z0-9A-Z]+)*@([a-z0-9A-Z]+[-|.])+[a-zA-Z]{2,5}$/,
  idCardReg : /^(([1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{4})|([1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|(X|x))))$/,
  phoneReg : /^1[34578]\d{9}$/,
  accountReg : /^(3[0-1][0-9]0[0-9]0\d{4})$/,
}

export default utils
