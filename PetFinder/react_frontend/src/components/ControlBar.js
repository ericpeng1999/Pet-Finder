import PropTypes from 'prop-types'

export const ControlBar = ({info, click}) => {
    return(
        <div>
            <div className='btn'>
                <button onClick={()=>click[1](info['type'], 1)}>first page</button>
            </div>
            <div className='btn'>
                <button onClick={()=>click[1](info['type'], info['page']-1)}>&lt;</button>
            </div>
            <div className='btn'>
                <button>{"Page: "+info['page']}</button>
            </div>
            <div className='btn'>
                <button onClick={()=>click[1](info['type'], info['page']+1)}>&gt;</button>
            </div>
            <div className='btn'>
                <button onClick={()=>click[1](info['type'], info['lastPage'])}>last page</button>
            </div>
        </div>
    )
}
ControlBar.propTypes = {
    info: PropTypes.shape({
        type: PropTypes.string,
        page: PropTypes.number,
        lastPage: PropTypes.number,
    }),
    clicks: PropTypes.arrayOf(PropTypes.func),
}