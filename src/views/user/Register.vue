<template>
  <div>
    <div class="crumbs crumbs-register">
      <el-breadcrumb separator="/" class="register-title">
        <el-breadcrumb-item>
          <i class="el-icon-user"></i><span>注册新账号</span>
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="userContent">
      <el-form ref="registerForm" status-icon :model="registerForm" :rules="registerRules" label-width=" 80px">

        <el-form-item prop="name" label="姓名">
          <el-input v-model="registerForm.name" placeholder="请输入您的姓名"></el-input>
        </el-form-item>

        <el-form-item prop="account" label="账号">
          <el-input v-model="registerForm.account" placeholder="请输入账号 ( 工号 / 病历号 )"></el-input>
        </el-form-item>

        <el-form-item prop="email" label="邮箱">
          <el-input v-model="registerForm.email" placeholder="请输入您的注册邮箱"></el-input>
        </el-form-item>

        <el-form-item prop="pass" label="密码">
          <el-input
            v-model="registerForm.pass"
            type="password"
            placeholder="请输入密码"
          ></el-input>
        </el-form-item>

        <el-form-item prop="checkPass" label="确认密码">
          <el-input
            v-model="registerForm.checkPass"
            type="password"
            placeholder="请再次输入密码"
          ></el-input>
        </el-form-item>

        <el-form-item prop="role" label="身份">
          <el-select
            class="select-role"
            v-model="registerForm.role"
            placeholder="请选择您的身份"
          >
            <el-option label="病患或家属" value="patient"></el-option>
            <el-option label="医务工作者" value="doctor"></el-option>
            <el-option label="系统管理员" value="manager"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item>
          <el-button :loading="loading" type="primary" @click="handleSubmit()">提交</el-button>
          <el-button @click="handleCancel()">返回</el-button>
        </el-form-item>

      </el-form>

    </div>
  </div>
</template>

<script>
import Util from "@/utils/utils";
import { userRegister } from "@/api/user";
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error("密码长度至少为6"));
      } else {
        if (this.registerForm.checkPass !== "") {
          this.$refs.registerForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validateCheckPass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else 
      if (value !== this.registerForm.pass) {
        callback(new Error("两次输入的密码不一致"));
      } else {
        callback();
      }
    };
    var validateEmail = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入邮箱"));
      } else 
      if (!Util.emailReg.test(value)) {
        callback(new Error("请输入正确的邮箱"));
      } else {
        callback();
      }
    };
    var validateAccount = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账号"));
      } else 
      if(!Util.accountReg.test(value)) {
        callback(new Error("请输入正确的账号"));
      } else {
        callback();
      }
    };
    return {
      loading: false,
      registerForm: {
        name: "",
        account: "",
        pass: "",
        checkPass: "",
        email: "",
        role: "",
      },
      registerRules: {
        name: [{ required: true, message: "请输入用户名", trigger: "blur" }],
        account: [{ required: true, validator: validateAccount, trigger: "blur" }],
        pass: [{ required: true, validator: validatePass, trigger: "blur" }],
        checkPass: [{ required: true, validator: validateCheckPass, trigger: "blur" }],
        email: [{ required: true, validator: validateEmail, trigger: "blur" }],
        role: [{ required: true, message: "请确定您的身份", trigger: "blur" }],
      },
    };
  },
  methods: {
    handleSubmit() {
      this.loading = true;

      this.$refs.registerForm.validate((valid) => {
        if (valid) {
          console.log("正在提交表单");
          this.loading = true;
          const data = { 
            name: this.registerForm.name,
            userID: this.registerForm.account,
            email: this.registerForm.email,
            passwd: this.registerForm.pass,
            role: this.registerForm.role,
           };
          userRegister(data)
          .then((res) => {
            // console.log(res.data);
            if(res.data.ifTrue) {
              // 后端注册成功
              this.$message.success("注册成功！将为您自动登录...");
              localStorage.setItem("ls_userID", this.registerForm.account);
              this.$router.push("/");
              this.loading = false;
            } else {
              // 后端返回false
              this.$message.error("注册失败，请联系系统管理员");
              this.loading = false;
            }
          })
          .catch(() => {
            // request返回error
            this.$message.error("注册失败，后端服务器超时");
            this.loading = false;
          });
        } else {
          // valid失败
          this.$message.error("提交失败，请检查输入后再试");
          this.loading = false;
          return false;
        }
      });
    },
    handleCancel() {
      this.$router.push("/login");
    },
  },
};
</script>

<style>
.crumbs-register {
  background-color: #eef1f6;
  height: 50px;
  line-height: 50px;
}
.register-title {
  line-height: 50px;
  margin: 0 auto;
  width: 100px;
  font-size: 16px;
}
.userContent {
  width: 400px;
  margin: 0 auto;
}

@media screen and (max-width: 500px) {
  .userContent {
    width: 250px;
  }
}

</style>