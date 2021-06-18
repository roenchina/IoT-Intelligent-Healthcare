import request from '@/utils/request';

export function getBasicStatic() {
  return request({
    url: '/data/getBasicStatic',
    method: 'get',
  });
}