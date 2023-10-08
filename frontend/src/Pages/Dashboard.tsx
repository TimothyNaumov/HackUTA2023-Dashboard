import AnalyticsBox from '../Components/AnalyticsBox';
import Incidents from '../Components/Incident';
import TitleBar from '../Components/TitleBar';
import './Dashboard.css';

const Dashboard = () => {

    return (
        <div className='mainContainer'>
            <div className='title'>
                <TitleBar />
            </div>
            <div className='splitScreen'>
                <div className='leftScreen'>
                    <Incidents />
                </div>
                <div className='rightScreen'>
                    <AnalyticsBox />
                </div>  
            </div>
        </div>
    )

}

export default Dashboard