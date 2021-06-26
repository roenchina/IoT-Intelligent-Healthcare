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
    method: 'post',
    data: data,
  });
}

// 给出数据的_ID，后端直接删除该条数据
// 返回ifTrue为是否删除成功
export function deleteData(data) {
  return request({
    url: '/data/deleteData',
    method: 'delete',
    data: data,
  });
}