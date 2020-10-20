import Vue from 'vue'

// Utilize default vue instance as app-scope bus for events
export const EventBus = new Vue()

export function isValidJwt (jwt: any) {
  // prelim check to jwt field length for validation
  if (!jwt || jwt.split('.').length < 3) {
    return false
  }
  const data = JSON.parse(atob(jwt.split('.')[1]))
  // Transform to Epoch to conform to JS datetime instance
  const exp = new Date(data.exp * 1000) 
  const now = new Date()
  return now < exp
}