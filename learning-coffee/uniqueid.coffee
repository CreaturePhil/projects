uniqueId = (length=8) ->
  id = ""
  id += Math.random().toString(36).substr(2) while id.length < length
  id.substr 0, length

console.log uniqueId()
console.log uniqueId(2)
console.log uniqueId(30)
console.log uniqueId(25)
console.log uniqueId(100)
