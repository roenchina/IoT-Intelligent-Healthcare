import request from '@/utils/request';

export function getBasicStatic() {
  return request({
    url: '/data/getBasicStatic',
    method: 'get',
  });
}

// data = {
//   limit: 20,
//   sort: "recent"
// }
export function getAllData(data) {
  return request({
    url: '/data/getAllData',
    method: 'get',
    data: data,
  });
}