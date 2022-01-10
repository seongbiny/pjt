# README

### UI 구성

1. **TodoTemplate** : 화면을 가운데에 정렬, 일정 관리를 보여준다. children으로 내부 JSX를 props로 받아와서 랜더링해 준다.
2. **TodoInsert** : 새로운 항목을 입력하고 추가할 수 있는 컴포넌트. state를 통해 인풋의 상태를 관리한다.
3. **TodoListItem** : 각 할 일 항목에 대한 정보를 보여준다. todo 객체를 props로 받아 와서 상태에 따라 다른 스타일의 UI를 보여준다.
4. **TodoList** : todos 배열을 props로 받아 온 후, 이를 배열 내장 함수 map을 사용해서 여러 개의 TodoListItem 컴포넌트로 변환하여 보여 준다.



```jsx
<TodoTemplate>
    <TodoInsert />
    <TodoList />
</TodoTemplate>
```



### App에서 todos 상태 사용하기

App에서 useState를 사용하여 todos라는 상태를 정의하고, todos를 TodoList의 props로 전달

```jsx
// App.js

import { useState } from 'react';

function App () {
    const [todos, setTodos] = useState([초기 데이터]);
    
    return (
      <TodoTemplate>
      <TodoInsert />
      <TodoList todos={todos} /> 
    </TodoTemplate>
    )
}

export default App;
```

TodoList에서 todos 값을 받아 온 후 TodoItem으로 변환하여 랜더링하도록 설정해야 한다.

```jsx
// TodoList.js

function TodoList ({ todos }){
    return (
        <div className="TodoList">
            {todos.map(todo =>(
                <TodoListItem todo={todo} key={todo.id} />
            ))}
        </div>
    )
}

export default TodoList;
```

props로 받아 온 todo 배열을 map을 통해 TodoListItem으로 이루어진 배열로 변환하여 랜더링해 주었다. todo 데이터는 통째로 props로 전달해 준다. 여러 종류의 값을 전달해야 하는 경우 객체로 통째로 전달하는 편이 나중에 성능 최적화를 할 때 편리하다.

TodoListItem 컴포넌트에서 받아 온 todo 값에 따라 제대로 된 UI를 보여줄 수 있도록 컴포넌트를 수정한다.

```jsx
// TodoListItem.js

...
function TodoListItem({ todo }){
    const { text, checked } = todo;
    
    return (
    <div className="TodoListItem">
            <div className={cn('checkbox', {checked})} onClick={() => onToggle(id)}>
                {checked ? <MdCheckBox /> : <MdCheckBoxOutlineBlank />}
                <div className="text">{text}</div>
            </div>
        </div>
    )
}
```

