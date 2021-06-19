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
    method: 'put',
    data: data,
  });
}

export function updateFacility(newdata) {
  return request({
    url: '/facility/updateFacility',
    method: 'put',
    data: newdata,
  });
}
