import PropTypes from 'prop-types'

const Header = ({entryNum, showSelect, onChange}) => {
  return (
    <header className='header'>
        <h1 style = {{color:"red"}}>"Pet Finder"</h1>
        {!showSelect && <select id="entriesPerRow" defaultValue={'2'} value={entryNum} onChange={(e)=>{onChange(e.target.value)}}>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
        </select>}
    </header>
  )
}
Header.propTypes = {
  entryNum: PropTypes.string,
  showSelect: PropTypes.bool,
  onChange: PropTypes.func,
}

// css in JS
// const headingStyle = {
//     color: "red",
//     backgroundColor: 'green'
// }

export default Header