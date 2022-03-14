import { useContext, useEffect, useState } from 'react'
import { UserInfoContext } from './_app'

export const Index = () => {
  const { users, setUsers } = useContext(UserInfoContext)

  const [editUser, setEditUser] = useState({
    name: '',
  })

  useEffect(() => {
    const name1 = 'test'
    setEditUser({ ...editUser, name: name1 })
    setUsers([...users, { name: editUser.name }])
  }, [])
  return <div>{editUser.name}</div>
}

export default Index
