# 模拟数据库权限
'''
# 组（角色）
"group":[
    {"id":1,"name":"editor","alias":"editor","level":0,"remark":"","parentId":0},
    {"id":2,"name":"auditor","alias":"auditor","level":0,"remark":"","parentId":0},
    {"id":3,"name":"visitor","alias":"visitor","level":0,"remark":"","parentId":0}
],

# 资源
"resource":[
    {"id":1,"name":"industry","alias":"industry","remark":"","disabled":false},
    {"id":2,"name":"company","alias":"company","remark":"","disabled":false},
    {"id":3,"name":"target","alias":"target","remark":"","disabled":false},
    {"id":4,"name":"report","alias":"report","remark":"","disabled":false},
    {"id":5,"name":"yearReportData","alias":"yearReportData","remark":"","disabled":false},
    {"id":6,"name":"socialReportData","alias":"socialReportData","remark":"","disabled":false},
    {"id":7,"name":"targetData","alias":"targetData","remark":"","disabled":false},
    {"id":8,"name":"publicSentiment","alias":"publicSentiment","remark":"","disabled":false},
    {"id":9,"name":"csrScore","alias":"csrScore","remark":"","disabled":false},
    {"id":10,"name":"audit","alias":"audit","remark":"","disabled":false}
],

# 操作
"action":[
    {"id":1,"name":"edit","alias":"edit","remark":"","disabled":false},
    {"id":2,"name":"delete","alias":"delete","remark":"","disabled":false},
    {"id":3,"name":"upload","alias":"upload","remark":"","disabled":false},
    {"id":4,"name":"download","alias":"download","remark":"","disabled":false},
    {"id":5,"name":"export","alias":"export","remark":"","disabled":false},
    {"id":6,"name":"audit","alias":"audit","remark":"","disabled":false}
],

# 资源操作关系
"resourceAction_relation":[
    {"id":5,"groupId":1,"groupAlias":"editor","resourceId":3,"resourceAlias":"target","actionId":1,"actionAlias":"edit"},
    {"id":6,"groupId":1,"groupAlias":"editor","resourceId":4,"resourceAlias":"report","actionId":2,"actionAlias":"delete"},
    {"id":7,"groupId":1,"groupAlias":"editor","resourceId":4,"resourceAlias":"report","actionId":3,"actionAlias":"upload"},
    {"id":8,"groupId":1,"groupAlias":"editor","resourceId":4,"resourceAlias":"report","actionId":4,"actionAlias":"download"},
    {"id":11,"groupId":1,"groupAlias":"editor","resourceId":5,"resourceAlias":"yearReportData","actionId":1,"actionAlias":"edit"},
    {"id":12,"groupId":1,"groupAlias":"editor","resourceId":6,"resourceAlias":"socialReportData","actionId":1,"actionAlias":"edit"},
    {"id":13,"groupId":1,"groupAlias":"editor","resourceId":7,"resourceAlias":"targetData","actionId":1,"actionAlias":"edit"},
    {"id":15,"groupId":1,"groupAlias":"editor","resourceId":7,"resourceAlias":"targetData","actionId":5,"actionAlias":"export"},
    {"id":16,"groupId":1,"groupAlias":"editor","resourceId":8,"resourceAlias":"publicSentiment","actionId":1,"actionAlias":"edit"},
    {"id":17,"groupId":1,"groupAlias":"editor","resourceId":8,"resourceAlias":"publicSentiment","actionId":1,"actionAlias":"export"},
    {"id":18,"groupId":1,"groupAlias":"editor","resourceId":9,"resourceAlias":"csrScore","actionId":5,"actionAlias":"export"},
    {"id":19,"groupId":2,"groupAlias":"auditor","resourceId":3,"resourceAlias":"target","actionId":1,"actionAlias":"edit"},
    {"id":20,"groupId":2,"groupAlias":"auditor","resourceId":4,"resourceAlias":"report","actionId":2,"actionAlias":"delete"},
    {"id":21,"groupId":2,"groupAlias":"auditor","resourceId":4,"resourceAlias":"report","actionId":3,"actionAlias":"upload"},
    {"id":22,"groupId":2,"groupAlias":"auditor","resourceId":4,"resourceAlias":"report","actionId":4,"actionAlias":"download"},
    {"id":29,"groupId":2,"groupAlias":"auditor","resourceId":9,"resourceAlias":"csrScore","actionId":5,"actionAlias":"export"},
    {"id":30,"groupId":2,"groupAlias":"auditor","resourceId":10,"resourceAlias":"audit","actionId":6,"actionAlias":"audit"},
    {"id":31,"groupId":2,"groupAlias":"auditor","resourceId":6,"resourceAlias":"socialReportData","actionId":1,"actionAlias":"edit"},
    {"id":32,"groupId":2,"groupAlias":"auditor","resourceId":6,"resourceAlias":"socialReportData","actionId":6,"actionAlias":"audit"},
    {"id":33,"groupId":2,"groupAlias":"auditor","resourceId":7,"resourceAlias":"targetData","actionId":1,"actionAlias":"edit"},
    {"id":34,"groupId":2,"groupAlias":"auditor","resourceId":7,"resourceAlias":"targetData","actionId":5,"actionAlias":"export"},
    {"id":35,"groupId":2,"groupAlias":"auditor","resourceId":7,"resourceAlias":"targetData","actionId":6,"actionAlias":"audit"},
    {"id":36,"groupId":2,"groupAlias":"auditor","resourceId":8,"resourceAlias":"publicSentiment","actionId":1,"actionAlias":"edit"},
    {"id":37,"groupId":2,"groupAlias":"auditor","resourceId":8,"resourceAlias":"publicSentiment","actionId":1,"actionAlias":"export"},
    {"id":38,"groupId":2,"groupAlias":"auditor","resourceId":8,"resourceAlias":"publicSentiment","actionId":6,"actionAlias":"audit"},
    {"id":39,"groupId":2,"groupAlias":"auditor","resourceId":5,"resourceAlias":"yearReportData","actionId":1,"actionAlias":"edit"},
    {"id":40,"groupId":2,"groupAlias":"auditor","resourceId":5,"resourceAlias":"yearReportData","actionId":6,"actionAlias":"audit"}
    {"id":41,"groupId":3,"groupAlias":"visitor","resourceId":4,"resourceAlias":"report","actionId":4,"actionAlias":"download"},
]
'''

RESOURCE_PERMISSION_DIC = {  # {groupId: resourcePermissions}
    1: [  # editor
        {"id": 1, "name": "industry", "alias": "industry"},
        {"id": 2, "name": "company", "alias": "company"},
        {"id": 3, "name": "target", "alias": "target"},
        {"id": 4, "name": "report", "alias": "report"},
        {"id": 5, "name": "yearReportData", "alias": "yearReportData"},
        {"id": 6, "name": "socialReportData", "alias": "socialReportData"},
        {"id": 7, "name": "targetData", "alias": "targetData"},
        {"id": 8, "name": "publicSentiment", "alias": "publicSentiment"},
        {"id": 9, "name": "csrScore", "alias": "csrScore"},
    ],
    2: [  # audit人
        {"id": 1, "name": "industry", "alias": "industry"},
        {"id": 2, "name": "company", "alias": "company"},
        {"id": 3, "name": "target", "alias": "target"},
        {"id": 4, "name": "report", "alias": "report"},
        {"id": 5, "name": "yearReportData", "alias": "yearReportData"},
        {"id": 6, "name": "socialReportData", "alias": "socialReportData"},
        {"id": 7, "name": "targetData", "alias": "targetData"},
        {"id": 8, "name": "publicSentiment", "alias": "publicSentiment"},
        {"id": 9, "name": "csrScore", "alias": "csrScore"},
        {"id": 10, "name": "audit", "alias": "audit"}
    ],
    3: [  # visitor
        {"id": 1, "name": "industry", "alias": "industry"},
        {"id": 2, "name": "company", "alias": "company"},
        {"id": 3, "name": "target", "alias": "target"},
        {"id": 4, "name": "report", "alias": "report"},
        {"id": 5, "name": "yearReportData", "alias": "yearReportData"},
        {"id": 6, "name": "socialReportData", "alias": "socialReportData"},
        {"id": 7, "name": "targetData", "alias": "targetData"},
        {"id": 8, "name": "publicSentiment", "alias": "publicSentiment"},
        {"id": 9, "name": "csrScore", "alias": "csrScore"},
    ],
}

ACTION_PERMISSION_DIC = {  # {groupId: actionPermissions}
    1: [
        {"id": 5, "resourceId": 3, "resourceAlias": "target", "actionId": 1, "actionAlias": "edit"},
        {"id": 6, "resourceId": 4, "resourceAlias": "report", "actionId": 2, "actionAlias": "delete"},
        {"id": 7, "resourceId": 4, "resourceAlias": "report", "actionId": 3, "actionAlias": "upload"},
        {"id": 8, "resourceId": 4, "resourceAlias": "report", "actionId": 4, "actionAlias": "download"},
        {"id": 11, "resourceId": 5, "resourceAlias": "yearReportData", "actionId": 1, "actionAlias": "edit"},
        {"id": 12, "resourceId": 6, "resourceAlias": "socialReportData", "actionId": 1, "actionAlias": "edit"},
        {"id": 13, "resourceId": 7, "resourceAlias": "targetData", "actionId": 1, "actionAlias": "edit"},
        {"id": 15, "resourceId": 7, "resourceAlias": "targetData", "actionId": 5, "actionAlias": "export"},
        {"id": 16, "resourceId": 8, "resourceAlias": "publicSentiment", "actionId": 1, "actionAlias": "edit"},
        {"id": 17, "resourceId": 8, "resourceAlias": "publicSentiment", "actionId": 1, "actionAlias": "export"},
        {"id": 18, "resourceId": 9, "resourceAlias": "csrScore", "actionId": 5, "actionAlias": "export"},
    ],
    2: [
        {"id": 19, "resourceId": 3, "resourceAlias": "target", "actionId": 1, "actionAlias": "edit"},
        {"id": 20, "resourceId": 4, "resourceAlias": "report", "actionId": 2, "actionAlias": "delete"},
        {"id": 21, "resourceId": 4, "resourceAlias": "report", "actionId": 3, "actionAlias": "upload"},
        {"id": 22, "resourceId": 4, "resourceAlias": "report", "actionId": 4, "actionAlias": "download"},
        {"id": 29, "resourceId": 9, "resourceAlias": "csrScore", "actionId": 5, "actionAlias": "export"},
        {"id": 30, "resourceId": 10, "resourceAlias": "audit", "actionId": 6, "actionAlias": "audit"},
        {"id": 31, "resourceId": 6, "resourceAlias": "socialReportData", "actionId": 1, "actionAlias": "edit"},
        {"id": 32, "resourceId": 6, "resourceAlias": "socialReportData", "actionId": 6, "actionAlias": "audit"},
        {"id": 33, "resourceId": 7, "resourceAlias": "targetData", "actionId": 1, "actionAlias": "edit"},
        {"id": 34, "resourceId": 7, "resourceAlias": "targetData", "actionId": 5, "actionAlias": "export"},
        {"id": 35, "resourceId": 7, "resourceAlias": "targetData", "actionId": 6, "actionAlias": "audit"},
        {"id": 36, "resourceId": 8, "resourceAlias": "publicSentiment", "actionId": 1, "actionAlias": "edit"},
        {"id": 37, "resourceId": 8, "resourceAlias": "publicSentiment", "actionId": 1, "actionAlias": "export"},
        {"id": 38, "resourceId": 8, "resourceAlias": "publicSentiment", "actionId": 6, "actionAlias": "audit"},
        {"id": 39, "resourceId": 5, "resourceAlias": "yearReportData", "actionId": 1, "actionAlias": "edit"},
        {"id": 40, "resourceId": 5, "resourceAlias": "yearReportData", "actionId": 6, "actionAlias": "audit"}
    ],
    3: [
        {"id": 41, "resourceId": 4, "resourceAlias": "report", "actionId": 4, "actionAlias": "download"},
    ]
}
