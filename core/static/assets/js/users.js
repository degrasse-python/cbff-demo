export const userList = [
  {
    type: 'betauser',
    beta_access: true
  },
  {
    type: 'normaluser',
    beta_access: false
  }
]

export const betaAccess = () => {
  if (localStorage.getItem('user') === null) {
    return false
  } else {
    let localUser = {}
    userList.map((user) => {
      if (user.type === localStorage.getItem('user')) {
        localUser = user
      }
    })
    return localUser.beta_access
  }
}

export const isLoggedIn = () => {
  return localStorage.getItem('user') !== null
}
