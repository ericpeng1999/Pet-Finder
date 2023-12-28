import {React, useState, useEffect} from 'react'
import Header from './components/Header'
import { AvaliableTypes} from './components/AvaliableTypes'
import { AnimalList } from './components/AnimalList'
import { AnimalDetailedPage } from './components/AnimalDetailedPage'

const App = () => {
  const [animalList, setAnimalList] = useState([])
  const [types, setTypes] = useState([])
  const [curAnimal, setCurAnimal] = useState([])

  const [showStates, setShowStates] = useState({"typeList": true, 'animalList': false, 'curAnimal': false})

  const [entryPerRow, setEntryPerRow] = useState('2')
  const [width, setWidth] = useState(47)
  const [infoCache, setInfoCache] = useState({'type': '', 'page': 1, 'lastPage': 1})

  const baseURL = "http://127.0.0.1:8000/"

  useEffect(() => {
    request(baseURL,setTypes)
  }, [])

  const updateWidth = (row) =>{
    setEntryPerRow(row)
    // the following magic numbers are got by experimenting
    if(row==='1') {
      setWidth(100)
    }else if (row==='2') {
      setWidth(47)
    }else if (row==='3') {
      setWidth(31)
    }else if (row==='4') {
      setWidth(22)
    }else{
        throw new Error("invalid width value encountered: entryPerRow="+row+" of type: "+typeof(row))
    }
  }

  const request = async (url, set) => {
    set(await (await fetch(url)).json())
  }

  const getHomePage = () => {
    setShowStates({"typeList": true, 'animalList': false, 'curAnimal': false})
  }

  const reset = async () => {
    await fetch(baseURL+'refresh')
  }

  const getAnimalList = async (type, page) => {
    if(page<1 || page>infoCache['lastPage']){
      return
    }
    const response = await (await fetch(`${baseURL}${type}/${page}/`)).json()
    setAnimalList(response[1])
    setInfoCache({'type': type, 'page': page, "lastPage": response[0]})
    setShowStates({"typeList": false, 'animalList': true, 'curAnimal': false})
  }

  const getAnimal = async (id) => {
    await request(`${baseURL}${infoCache['type']}/${infoCache['page']}/${id}/`, setCurAnimal)
    setShowStates({"typeList": false, 'animalList': false, 'curAnimal': true})
  }

  return(
    <div className='container'>
      <Header entryNum={entryPerRow} showSelect={showStates['curAnimal']} onChange={updateWidth}/>
      {showStates["typeList"] && <AvaliableTypes types={types} width={width} reset={reset} onClick={getAnimalList}/>}
      {showStates["animalList"] && <AnimalList info={infoCache} baseURL={baseURL} list={animalList} width={width} clicks={[getHomePage, getAnimalList, getAnimal]}/>}
      {showStates["curAnimal"] && <AnimalDetailedPage animal={curAnimal} info={infoCache} clicks={[getHomePage, getAnimalList, getAnimal]}/>}
    </div>
  );
}

export default App;
