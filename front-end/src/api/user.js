import request from '@/utils/request';

export function userVerify(data) {
  return request({
    url: '/user/userVerify',
    method: 'post',
    data: data,
  });
}

export function userRegister(data) {
  return request({
    url: '/user/userRegister',
    method: 'post',
    data: data,
  });
}