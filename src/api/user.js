import request from '@/utils/request';

// 测试成功
export function getName() {
  return request({
    url: '/user/getName',
    method: 'get',
  });
}

export function userVerify(data) {
  return request({
    url: '/user/userVerify',
    method: 'post',
    data: data,
  });
}
