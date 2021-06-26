import request from '@/utils/request';

// 获取所有设备信息
// 注意不包括名字为_null的设备
export function getAllFacility() {
  return request({
    url: '/facility/getAllFacility',
    method: 'get',
  });
}

// remove只是将改设备命名为_null
// 为了保证数据库完整性，并不删除该条记录
export function removeFacility(data) {
  return request({
    url: '/facility/removeFacility',
    method: 'post',
    data: data,
  });
}

// 传入新的一条数据
// 以facID为准，更新修改其他内容
export function updateFacility(newdata) {
  return request({
    url: '/facility/updateFacility',
    method: 'post',
    data: newdata,
  });
}

// 传入一条没有facID的新数据
// 想数据库中增加该条数据，并通过info.facID返回新分配的ID
export function addFacility(newdata) {
  return request({
    url: '/facility/addFacility',
    method: 'post',
    data: newdata,
  });
}

// export function getFacCount() {
//   return request({
//     url: '/facility/getFacCount',
//     method: 'get',
//   });
// }
