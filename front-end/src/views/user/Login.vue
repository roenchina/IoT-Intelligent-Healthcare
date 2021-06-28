<template>
  <div class="login-wrap">
    <div class="ms-login">
      <div class="ms-title">欢迎，请先登录</div>

      <el-form
        :model="loginForm"
        :rules="loginRules"
        ref="loginForm"
        label-width="0px"
        class="ms-content"
      >
        <el-form-item prop="userID">
          <el-input
            v-model="loginForm.userID"
            placeholder="userID"
            tabindex="1"
            type="text"
          >
            <template #prepend>
              <el-button icon="el-icon-user"></el-button>
            </template>
          </el-input>
        </el-form-item>

        <el-form-item prop="password">
          <el-input
            type="password"
            placeholder="password"
            tabindex="2"
            v-model="loginForm.password"
            @keyup.enter="submitForm()"
          >
            <template #prepend>
              <el-button icon="el-icon-lock"></el-button>
            </template>
          </el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="primary" @click="submitForm()">登录</el-button>
        </div>
        <div class="register-btn">
          <el-button type="info" plain @click="handleRegister()"
            >没有账号？注册</el-button
          >
        </div>
        <!-- <p class="login-tips">Tips : 用户名和密码随便填。</p> -->
        <!-- <router-link  to="/register">点这里跳转</router-link> -->
      </el-form>
    </div>
  </div>
</template>

<script>
import { userVerify } from "@/api/user";
export default {
  data() {
    return {
      loginForm: {
        userID: "3180105412",
        password: "123456",
      },
      loginRules: {
        userID: [{ required: true, message: "请输入账号", trigger: "blur" }],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  created() {},
  methods: {
    submitForm() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          const data = {
            userID: this.loginForm.userID,
            passwd: this.loginForm.password,
          };
          userVerify(data).then((res) => {
            // console.log("when login-----------");
            // console.log(res.data.ifTrue);
            if (res.data.ifTrue) {
              // 验证成功
              this.$message.success("登录成功！");
              // 根据从res中的结果，将用户基本信息存到localStorage中，维护登录状态
              localStorage.setItem("ls_userID", this.loginForm.userID);
              localStorage.setItem("ls_userName", res.data.userInfo.name);
              localStorage.setItem("ls_userRole", res.data.userInfo.role);
              localStorage.setItem("ls_userEmail", res.data.userInfo.email);
              this.$router.push("/");
            } else {
              this.$message.error("用户密码不匹配，请检查后再次输入。");
            }
          });
        } else {
          this.$message.error("请输入账号和密码后重试。");
          return false;
        }
      });
    },
    handleRegister() {
      this.$router.push("/register");
    },
  },
};
</script>

<style scoped>
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  /* background-image: url(../assets/img/login-bg.jpg); */
  background-size: 100%;
}
.ms-title {
  width: 100%;
  line-height: 50px;
  text-align: center;
  font-size: 20px;
  color: #fff;
  border-bottom: 1px solid #ddd;
}
.ms-login {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 350px;
  margin: -190px 0 0 -175px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.3);
  overflow: hidden;
}
.ms-content {
  padding: 30px 30px;
}
.login-btn {
  text-align: center;
}
.login-btn button {
  width: 100%;
  height: 36px;
  margin-bottom: 10px;
}
.register-btn {
  text-align: center;
}
.register-btn button {
  width: 100%;
  height: 36px;
  margin-bottom: 10px;
}
.login-tips {
  font-size: 12px;
  line-height: 30px;
  color: #fff;
}
</style>