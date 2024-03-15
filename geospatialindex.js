db..student.createIndex({"score":"2dsphere"},
  {
  			"createdCollectionAutomatically": false,
  			"numIdexesBefore":1,
  			"numIndexesAfter":2,
  			"ok":1
  })

  < score_2dsphere
  > db.student.getIndexes()

  /*[
    { v: 2, key: { _id: 1 }, name: '_id_' },
    { v: 2, key: { class_id: 551 }, name: 'class_id_551' },
    {
      v: 2,
      key: { student_id: 777777, class_id: 551 },
      name: 'student_id_777777_class_id_551'
    },
    { v: 2, key: { student_id: 223344 }, name: 'student_id_223344' },
    { v: 2, key: { student: 1 }, name: 'student_1' },
    { v: 2, key: { products: 1 }, name: 'products_1' },
    {
      v: 2,
      key: { score: '2dsphere' },
      name: 'score_2dsphere',
      '2dsphereIndexVersion': 3
    }
  ]*/
