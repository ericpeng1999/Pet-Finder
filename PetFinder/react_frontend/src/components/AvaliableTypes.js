import PropTypes from 'prop-types'
import {Type} from "./Type"

export const AvaliableTypes = ({types, width, reset, onClick}) => {
    return (
        <div>
            <button onClick={()=>reset()}>refresh database</button>
            <div>
                {types.map((type) => (
                    <Type type={type} width={width} onClick={onClick}/>
                ))}
            </div>
        </div>
    )
}
AvaliableTypes.propTypes = {
    types: PropTypes.arrayOf(PropTypes.string),
    width: PropTypes.number,
    reset: PropTypes.func,
    onClick: PropTypes.func,
}