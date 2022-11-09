@app.get("/api/patients/{id}")
async def get_patient(id: int, headers: dict):
    return await patients_service.find_one(id)

@app.patch("/api/patients/{id}/treatment_name")
async def add_or_update_treatment_name(
    id: int,
    add_treatment_name_dto: AddTreatmentNameDto,
    headers: dict,
):
    return await patients_service.add_or_update_treatment_name(
        id, add_treatment_name_dto
    )


@app.get("/api/patients/{id}/treatment_skus")
async def get_treatment_skus(id: int, headers: dict):
    return await patients_service.get_treatment_skus(id)


@app.get("/api/patients/{id}/insurance_flow")
async def get_insurance_flow_details(id: int, headers: dict):
    response = await patients_service.get_insurance_flow_details(id)
    if response.status != 200:
        return response
    return response.patient


@app.get("/api/patients/{id}/discharge_flow")
async def get_discharge_flow_details(id: int, headers: dict):
    response = await patients_service.get_discharge_flow_details(id)
    if response.status != 200:
        return response
    return response.patient


@app.get("/api/patients/{id}/cost_summary")
async def get_cost_summary(id: int, headers: dict):
    response = await patients_service.get_cost_summary(id)
    if response.status != 200:
        return response
    return response.patient


@app.get("/api/patients/{id}/registration_complete")
async def registration_complete(id: int, headers: dict):
    return await patients_service.registration_complete(id)