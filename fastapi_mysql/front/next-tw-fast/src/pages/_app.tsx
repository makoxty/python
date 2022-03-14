import { AppProps } from 'next/app'
import { createContext, useState } from 'react'

export interface User {
  name: string
}

interface PropertyTypeContext {
  users: User[]
  setUsers: React.Dispatch<React.SetStateAction<User[]>>
}

const initialState: User[] = []

export const UserInfoContext = createContext({} as PropertyTypeContext)

const App = ({ Component, pageProps }: AppProps) => {
  const [users, setUsers] = useState(initialState)
  return (
    <UserInfoContext.Provider value={{ users, setUsers }}>
      <Component {...pageProps} />
    </UserInfoContext.Provider>
  )
}
export default App
