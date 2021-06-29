import axios from 'axios';

const service = axios.create({
  // baseURL: 'https://www.fastmock.site/mock/a0cc96cc05f3c016f468e87d4c253777/2021iot',
  baseURL: 'http://127.0.0.1:5000',
  timeout: 5000
});

service.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    console.log(error);
    return Promise.reject();
  }
);

service.interceptors.response.use(
  response => {
    // if (response.status === 200) {
      return response.data;
    // } else {
    //   Promise.reject();
    // }
  },
  error => {
    console.log(error);
    return Promise.reject();
  }
);

export default service;
