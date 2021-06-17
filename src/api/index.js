import request from '@/utils/request';

export const fetchData = query => {
  return request({
    url: './table.json',
    method: 'get',
    params: query
  });
};

// 测试成功
export function getName() {
  return request({
    url: '/user/getName',
    method: 'post',
  });
}