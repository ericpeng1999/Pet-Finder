import PropTypes from 'prop-types'
import { SmallProfile } from './AnimalSmallProfile'
import { ControlBar } from './ControlBar'

export const AnimalList = ({info, list, width, clicks}) => {
    return(
        <div>
            <div>
                <button onClick={()=>clicks[0]()}>return</button>
            </div>
            {list.map((ele) => (            
                <SmallProfile width={width} onClick={clicks[2]} ele={ele}/>
            ))}
            <ControlBar info={info} click={clicks}/>
        </div>
    )
}
AnimalList.propTypes = {
    info: PropTypes.shape({
        'type': PropTypes.string,
        'page': PropTypes.number,
        'lastPage': PropTypes.number,
    }),
    list: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number,
            name: PropTypes.string,
            description: PropTypes.string,
            imgURL: PropTypes.string,
        })
    ),
    width: PropTypes.number,
    onClick: PropTypes.arrayOf(PropTypes.func),
}